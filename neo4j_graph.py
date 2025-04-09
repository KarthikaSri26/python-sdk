from neo4j import GraphDatabase

# Connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "kskb2426"  # Replace this with your actual Neo4j DB password

# Connect to the database
driver = GraphDatabase.driver(uri, auth=(username, password))

# Function to create nodes and relationship
def create_graph(tx):
    tx.run("CREATE (a:Person {name: 'Alice'})-[:KNOWS]->(b:Person {name: 'Bob'})")

# Execute the function
with driver.session() as session:
    session.write_transaction(create_graph)

print("✅ Graph created successfully!")

driver.close()
