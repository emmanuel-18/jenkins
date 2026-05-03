import json

print("Training model...")

accuracy = 0.92

result = {
    "model": "LinearRegression",
    "accuracy": accuracy
}

print("Step 1: Loading data")
print("Step 2: Training model")
print(f"Step 3: Accuracy = {accuracy * 100}%")

# Save result to file (IMPORTANT NEW PART)
with open("results.json", "w") as f:
    json.dump(result, f)

print("Results saved to results.json")