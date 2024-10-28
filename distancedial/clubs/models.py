from django.db import models

class Club(models.Model):
    # Woods
    DRIVER = 'DR'
    THREE_WOOD = '3W'
    FIVE_WOOD = '5W'
    SEVEN_WOOD = '7W'
    
    # Irons
    TWO_IRON = '2I'
    THREE_IRON = '3I'
    FOUR_IRON = '4I'
    FIVE_IRON = '5I'
    SIX_IRON = '6I'
    SEVEN_IRON = '7I'
    EIGHT_IRON = '8I'
    NINE_IRON = '9I'
    
    # Wedges with lofts
    PITCHING_WEDGE = 'PW'  # ~46°
    GAP_WEDGE_50 = '50'    # 50°
    GAP_WEDGE_52 = '52'    # 52°
    SAND_WEDGE_54 = '54'   # 54°
    SAND_WEDGE_56 = '56'   # 56°
    LOB_WEDGE_58 = '58'    # 58°
    LOB_WEDGE_60 = '60'    # 60°
    LOB_WEDGE_62 = '62'    # 62°
    
    # Hybrids
    TWO_HYBRID = '2H'
    THREE_HYBRID = '3H'
    FOUR_HYBRID = '4H'
    FIVE_HYBRID = '5H'
    
    # Utility
    UTILITY_IRON = 'UI'

    CLUB_CHOICES = [
        # Woods
        (DRIVER, 'Driver'),
        (THREE_WOOD, '3 Wood'),
        (FIVE_WOOD, '5 Wood'),
        (SEVEN_WOOD, '7 Wood'),
        
        # Irons
        (TWO_IRON, '2 Iron'),
        (THREE_IRON, '3 Iron'),
        (FOUR_IRON, '4 Iron'),
        (FIVE_IRON, '5 Iron'),
        (SIX_IRON, '6 Iron'),
        (SEVEN_IRON, '7 Iron'),
        (EIGHT_IRON, '8 Iron'),
        (NINE_IRON, '9 Iron'),
        
        # Wedges
        (PITCHING_WEDGE, 'Pitching Wedge (46°)'),
        (GAP_WEDGE_50, '50° Wedge'),
        (GAP_WEDGE_52, '52° Wedge'),
        (SAND_WEDGE_54, '54° Wedge'),
        (SAND_WEDGE_56, '56° Wedge'),
        (LOB_WEDGE_58, '58° Wedge'),
        (LOB_WEDGE_60, '60° Wedge'),
        (LOB_WEDGE_62, '62° Wedge'),
        
        # Hybrids
        (TWO_HYBRID, '2 Hybrid'),
        (THREE_HYBRID, '3 Hybrid'),
        (FOUR_HYBRID, '4 Hybrid'),
        (FIVE_HYBRID, '5 Hybrid'),
        
        # Utility
        (UTILITY_IRON, 'Utility Iron'),
    ]

    club_type = models.CharField(max_length=2, choices=CLUB_CHOICES)

class Bag(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    clubs = models.ManyToManyField(Club)

    def __str__(self):
        return f"{self.user.username}'s Bag"