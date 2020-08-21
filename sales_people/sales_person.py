import random

import names

from leads.leads import Lead


class SalesPerson:
    amount_sold = 0
    amount_leads_contacted = 0
    total_contact_cost = 0

    def __init__(self, name, contact_method, sales_budget):
        self.name = name
        self.contact_method = contact_method
        self.sales_budget = sales_budget

    def work(self):
        print(f"my name is {self.name}, i can be contacted by {self.contact_method}")


class TiedAgent(SalesPerson):
    def __init__(self, name, sales_budget, contact_cost, conversion_skill=0.0):
        super().__init__(name, "Meeting", sales_budget)
        self.conversion_skill = conversion_skill
        self.contact_cost = contact_cost

    def contact_lead(self, lead: Lead):
        if lead.contacted:
            print("Lead already contacted")
        lead.contact(self.conversion_skill)
        self.total_contact_cost += self.contact_cost
        if lead.sold:
            self.amount_sold += lead.sales_potential


class CustomerService(SalesPerson):
    def __init__(self, name, sales_budget, contact_cost, conversion_skill=0.0):
        super().__init__(name, "Phone", sales_budget)
        self.conversion_skill = conversion_skill
        self.contact_cost = contact_cost

    def contact_lead(self, lead: Lead):
        if lead.contacted:
            print("Lead already contacted")
        lead.contact(self.conversion_skill)
        self.total_contact_cost += self.contact_cost
        if lead.sold:
            self.amount_sold += lead.sales_potential


def gen_random_agent(n_agent, agent_sales_budget, contact_cost, low_conversion_skill, high_conversion_skill):
    return [
        TiedAgent(names.get_full_name(),
                  agent_sales_budget,
                  contact_cost,
                  random.uniform(low_conversion_skill, high_conversion_skill))
        for _ in range(n_agent)
    ]


def gen_random_cs(n_cs, agent_sales_budget, contact_cost, low_conversion_skill, high_conversion_skill):
    return [
        CustomerService(names.get_full_name(),
                        agent_sales_budget,
                        contact_cost,
                        random.uniform(low_conversion_skill, high_conversion_skill))
        for _ in range(n_cs)
    ]
