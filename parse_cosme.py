Import xml.etree.ElementTree as ET

tree = ET.parse('https://www.biooo.cz/dataxml/heureka.php')

# Get the root element
root = tree.getroot()

# Loop through product elements (modify selector based on your feed structure)
for product in root.findall('product'):
  # Extract product name and brand
  name = product.find('name').text
  brand = product.find('brand').text

  # Print the extracted data (for now)
  print(f"Name: {name}, Brand: {brand}")
