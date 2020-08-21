from leads.leads import gen_random_leads
from organization.organization import Organization
from sales_people.sales_person import gen_random_agent, gen_random_cs

leads = gen_random_leads(10_000, 800, 10000)

agents = gen_random_agent(10, 10_000, 2000, 0.1, 0.25)
cs_people = gen_random_cs(30, 1000, 200, -0.1, 0.0)

all_personnel = agents + cs_people

my_org = Organization("AB", sales_people=all_personnel, leads=leads)

my_org.identify_personnel()
my_org.allocate_leads(0.75)

print(f"amount of leads in org {my_org.num_leads}")

print(f"number of people working in the org is {my_org.num_employees}")
my_org.sim_sales()

print(f"sales was {my_org.sales}")
print(f"cost was {my_org.contact_cost}")