from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([
    ('AdExposure', 'WebsiteExperience'),
    ('WebsiteExperience', 'Purchase'),
    ('ProductPrice', 'Purchase')
])

cpd_ad = TabularCPD(
    variable='AdExposure',
    variable_card=2,
    values=[[0.6], [0.4]]
)

cpd_website = TabularCPD(
    variable='WebsiteExperience',
    variable_card=2,
    values=[
        [0.8, 0.4],
        [0.2, 0.6]
    ],
    evidence=['AdExposure'],
    evidence_card=[2]
)

cpd_price = TabularCPD(
    variable='ProductPrice',
    variable_card=2,
    values=[[0.55], [0.45]]
)

cpd_purchase = TabularCPD(
    variable='Purchase',
    variable_card=2,
    values=[
        [0.9, 0.7, 0.6, 0.2],
        [0.1, 0.3, 0.4, 0.8]
    ],
    evidence=['WebsiteExperience', 'ProductPrice'],
    evidence_card=[2, 2]
)

model.add_cpds(cpd_ad, cpd_website, cpd_price, cpd_purchase)

print(model.check_model())

inference = VariableElimination(model)

result = inference.query(
    variables=['Purchase'],
    evidence={
        'AdExposure': 0,
        'WebsiteExperience': 0,
        'ProductPrice': 1
    }
)

print(result)