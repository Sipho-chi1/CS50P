def nutrition():
    item=input('Item: ').strip().lower()
    nutritions={'apple':130,
                'avocado':50,
                'banana':110,
                'cantaloupe':50,
                'grapefruit':60,
                'grapes':90,
                'honeydew melon':50,
                'kiwifruit':90,
                'lemon':15,
                'nectarine':60,
                'orange':80,
                'peach':60,
                'pear':100,
                'plums':70,
                'strawberries':50,
                'sweet cherries':100,
                'tangerine':50,
                'watermelon':80}
    if item in nutritions:
        print('Calories: ',nutritions[item])
nutrition()