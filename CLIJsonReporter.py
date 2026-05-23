import json

with open("dummy.json",'r') as file:
    result = json.load(file)

metrics = result['metrics']
params = result['training_parameters']

print("==================================================\n📈 MACHINE LEARNING METRICS REPORT\n==================================================")
print(f"Project Name: {result['project_name']}")
print(f"Framework: {result['framework']}")

print("\n[TRAINING PARAMS]\n--------------------------------------------------")

print(f"Epochs: {params['epochs']}")
print(f"Learning Rate: {params['learning_rate']:.5f}")
print(f"Batch Size: {params['batch_size']}")

print("\n[EVALUATION METRICS]\n--------------------------------------------------")

if metrics['accuracy'] > 0.90:
    print(f"Accuracy: {metrics['accuracy'] * 100} % *")
else:
    print(f"Accuracy: {metrics['accuracy'] * 100}% ")

print(f"Precision: {metrics['precision']}")
print(f"Recall: {metrics['recall']}")
print(f"Loss: {metrics['loss']}")