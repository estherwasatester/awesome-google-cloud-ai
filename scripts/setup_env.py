import csv
import sys
import os
import json

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 setup_env.py <product1> <product2> ...")
        sys.exit(1)

    products_requested = [p.lower() for p in sys.argv[1:]]
    csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'maad_stack.csv')
    
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found.")
        sys.exit(1)

    required_mcps = set()
    required_extensions = set()
    required_skills = set()

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_name = row.get('Product', '').strip().lower()
            
            # Check if this row matches any of the requested products
            # Support partial matching or exact matching
            is_match = False
            for req in products_requested:
                if req in product_name:
                    is_match = True
                    break
            
            if is_match:
                mcp = row.get('MCP Server (GitHub)', '').strip()
                if mcp:
                    for item in mcp.split(','):
                        required_mcps.add(item.strip())
                
                ext = row.get('Gemini CLI Extension', '').strip()
                if ext:
                    for item in ext.split(','):
                        required_extensions.add(item.strip())
                
                skills = row.get('Agent Skills', '').strip()
                if skills:
                    for item in skills.split(','):
                        required_skills.add(item.strip())

    print(json.dumps({
        "mcp_servers": list(required_mcps),
        "extensions": list(required_extensions),
        "agent_skills": list(required_skills)
    }, indent=2))

if __name__ == '__main__':
    main()
