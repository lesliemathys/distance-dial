from django.db.models import Avg
from django.db.models.functions import ExtractDate
import numpy as np
from practice_sessions.models import Shot
from clubs.models import Club
from collections import defaultdict

def calculate_club_stats(user):
    """
    Calculate median and mean distances for all clubs in user's bag.
    
    Args:
        user: User object
    
    Returns:
        dict: Contains overall stats for each club
        {
            'DR': {
                'median': 240.5,
                'mean': 238.2,
                'count': 30
            },
            ...
        }
    """
    stats = {}
    
    # Get all non-deleted shots for user
    user_shots = Shot.objects.filter(
        session__user=user,
        is_deleted=False,
        session__is_deleted=False
    )
    
    # Group shots by club
    club_shots = defaultdict(list)
    for shot in user_shots:
        club_shots[shot.club.club_type].append(float(shot.distance))
    
    # Calculate stats for each club
    for club_type, distances in club_shots.items():
        distances_array = np.array(distances)
        stats[club_type] = {
            'median': float(np.median(distances_array)),
            'mean': float(np.mean(distances_array)),
            'count': len(distances),
        }
    
    return stats

def get_club_trends(user, club_type):
    """
    Get chronological distance trends for a specific club.
    
    Args:
        user: User object
        club_type: String of club type (e.g., 'DR' for driver)
    
    Returns:
        dict: Contains lists of dates and corresponding stats
        {
            'dates': ['2024-01-01', '2024-01-02', ...],
            'distances': [240.5, 238.2, ...],
            'running_median': [240.5, 239.35, ...],
            'running_mean': [240.5, 239.35, ...]
        }
    """
    # Get chronological shots for this club
    club_shots = Shot.objects.filter(
        session__user=user,
        club__club_type=club_type,
        is_deleted=False,
        session__is_deleted=False
    ).order_by('session__session_datetime')
    
    if not club_shots:
        return None
    
    # Initialize data structures
    dates = []
    distances = []
    running_median = []
    running_mean = []
    
    # Build time series data
    current_distances = []
    for shot in club_shots:
        current_distances.append(float(shot.distance))
        dates.append(shot.session.session_datetime.strftime('%Y-%m-%d'))
        distances.append(float(shot.distance))
        running_median.append(float(np.median(current_distances)))
        running_mean.append(float(np.mean(current_distances)))
    
    return {
        'dates': dates,
        'distances': distances,
        'running_median': running_median,
        'running_mean': running_mean
    }

def get_club_gaps(user):
    """
    Calculate gaps between clubs based on median distances.
    
    Args:
        user: User object
    
    Returns:
        list: Contains sorted club stats with gaps
        [
            {
                'club_type': 'DR',
                'median': 240.5,
                'gap_to_next': 15.5
            },
            ...
        ]
    """
    # Get basic stats for all clubs
    club_stats = calculate_club_stats(user)
    
    # Convert to list and sort by median distance
    sorted_clubs = sorted(
        [{'club_type': k, **v} for k, v in club_stats.items()],
        key=lambda x: x['median'],
        reverse=True
    )
    
    # Calculate gaps
    for i in range(len(sorted_clubs) - 1):
        sorted_clubs[i]['gap_to_next'] = (
            sorted_clubs[i]['median'] - sorted_clubs[i + 1]['median']
        )
    
    # Last club has no gap
    if sorted_clubs:
        sorted_clubs[-1]['gap_to_next'] = 0
        
    return sorted_clubs