import ollama

# Load the multimodal (vision+text) model
# Make sure you have 'llava' or similar model pulled: `ollama pull llava`
model_name = "gemma3:4b-it-qat"  # or your specific multimodal model installed

# Path to your local image
image_path = "image/web_app.png"

# Your user question
prompt = """
    Review the provided AWS architecture diagram carefully.

    Your tasks:

        Extract all AWS services, resources, security layers, monitoring components, and networking infrastructure.

        For each service or component, output:

        provider: "AWS"

        service: (e.g., EC2, S3, Lambda, RDS, VPC, IAM, CloudWatch, etc.)

        type: (Compute, Storage, Networking, Database, Security, Monitoring, Messaging, etc.)

        metadata: (optional, e.g., region, availability zone, instance type, runtime, storage class, CIDR, security group IDs, IAM role names, notes, confidence)

        Identify and extract all logical connections and relationships:

        source: (name of the source component)

        target: (name of the target component)

        relationship: (contains, hosts, connects_to, invokes, routes_through, attached, monitored_by, secured_by, triggers)

    Important Rules:

        Treat VPCs, subnets, internet gateways, NAT gateways, availability zones, IAM roles, security groups, and CloudWatch alarms/log groups as valid components.

        Use "confidence": "low" in metadata if any service or connection is uncertain.

        Clearly model data flows, triggers, and deployments where possible.

    Output Format (only valid JSON, no markdown, no explanation):

        {
        "services": [...],
        "connections": [...]
        }
    """

# Open the image and send it along with prompt
with open(image_path, "rb") as f:
    image_bytes = f.read()

response = ollama.chat(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": prompt,
            "images": [image_bytes],  # 👈 Attach image here
        }
    ]
)

# Print the assistant's answer
print(response['message']['content'])
