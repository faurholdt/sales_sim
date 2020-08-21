import random


class Lead:
    contacted = False
    sold = False

    def __init__(self, sales_potential):
        self.sales_potential = sales_potential

    def contact(self, salesperson_skill=0):
        self.contacted = True
        if random.random()+salesperson_skill > random.random():
            self.sold = True


def gen_random_leads(n_leads, low, high):
    return [Lead(random.randint(low, high)) for _ in range(n_leads)]