import requests
import re
from bs4 import BeautifulSoup


# Open the schemas tree and grab the links to all the schema descriptions
path = 'https://schema.org%s'

r = requests.get(path%'/docs/full.html')
html = r.text

soup = BeautifulSoup(html, 'html.parser')

schema_links = [
    s['href'] for s in soup.find(id='full_thing_tree').find_all('a')
    if '/' in s['href']
]



# Iterate through all the schema descriptions and
# grab the properties and property descriptions

schemas = dict()

for i, slink in enumerate(schema_links):
    schemas[slink[1:]] = {'props': []}

    soup = BeautifulSoup(requests.get(path%slink).text, 'html.parser')
    props = soup.find_all("table", {"class": 'definition-table'})[0]
    props = props.find_all("tr", {"resource": True})

    for j, prop in enumerate(props):
        propName = prop.find('th', {'class': 'prop-nam'}).text.strip()
        propType = prop.find('td', {'class': 'prop-ect'}).text.strip()
        propDesc = prop.find('td', {'class': 'prop-desc'}).text.strip()

        schemas[slink[1:]]['props'].append([propName, propType, propDesc])

    break


# Write the schemas to pydantic classes
with open('test.py', 'w+') as f:
    f.write('\n'.join([
        'from pydantic import BaseModel, Field, AnyHttpUrl',
        'from uuid import UUID',
        'from typing import Union'
    ]))


base_class = '''
class {}(BaseModel):
    """
    {}
    """
    {}
'''

print(base_class)

base_prop = '''
    {}: {} = Field({}
        description="{}"
    )
'''

required_props = {'name'}
type_map = {
    'Text': 'str',
    'URL': 'AnyHttpUrl'
}

def convertType(propType):
    if 'or' in propType:
        typeSet = set()
        for s in propType.split('or'):
            t = s.strip()
            if t in schemas:
                typeSet.add(type_map.setdefault(t, t))
            else:
                typeSet.add(type_map.setdefault(t, 'str'))

        return 'Union[%s]'%(','.join(typeSet))

    else:
        if propType in schemas:
            return type_map.setdefault(propType, propType)
        else:
            return type_map.setdefault(propType, 'str')



for key, val in schemas.items():
    propsStr = []

    for propName, propType, propDesc in val['props']:
        required = 'None,' if propName not in required_props else ''
        propsStr.append(
            base_prop.format(
                propName,
                convertType(propType),
                required,
                propDesc
            )
        )

    classStr = base_class.format(key, key, '\n'.join(propsStr))

    print(classStr)

    with open('test.py', 'a') as f:
        f.write(classStr)

    break


from test import Thing

print(Thing.schema_json(indent=2))
