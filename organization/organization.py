import random
from typing import List

from leads.leads import Lead
from sales_people.sales_person import SalesPerson, TiedAgent, CustomerService


class Organization:
    agents = []
    cs_persons = []
    agent_leads = []
    cs_leads = []

    def __init__(self, org_name: str, sales_people: List[SalesPerson], leads: List[Lead]):
        self.org_name = org_name
        self.sales_people = sales_people
        self.leads = leads

    def work(self):
        for sales_person in self.sales_people:
            sales_person.work()

    @property
    def sales(self):
        sales = 0
        for person in self.sales_people:
            sales += person.amount_sold
        return sales

    @property
    def contact_cost(self):
        cost = 0
        for person in self.sales_people:
            cost += person.total_contact_cost
        return cost

    @property
    def num_employees(self):
        return len(self.sales_people)

    @property
    def num_leads(self):
        return len(self.leads)

    def allocate_leads(self, split: float):
        split_point = len(self.leads) * split
        self.agent_leads = self.leads[:int(split_point)]
        self.cs_leads = self.leads[int(split_point):]
        print(f"Leads has been assigned with a {split} split"
              f"{len(self.agent_leads)} was assigned to agents, {len(self.cs_leads)} was assigned to customer service"
              )

    def identify_personnel(self):
        for person in self.sales_people:
            if isinstance(person, TiedAgent):
                self.agents.append(person)
            if isinstance(person, CustomerService):
                self.cs_persons.append(person)

    def _get_lead(self, salesperson: SalesPerson):
        if isinstance(salesperson, TiedAgent):
            return self.agent_leads.pop(0)
        if isinstance(salesperson, CustomerService):
            return self.cs_leads.pop(0)

    def sim_sales(self):
        while self.agent_leads:
            agent = random.choice(self.agents)
            lead = self._get_lead(agent)
            agent.contact_lead(lead)
        while self.cs_leads:
            cs = random.choice(self.cs_persons)
            lead = self._get_lead(cs)
            cs.contact_lead(lead)

    def __repr__(self):
        return f"<{self.org_name}>"
