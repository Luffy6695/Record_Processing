import pandas as pd
df=pd.read_json("records.json")
required=["id","source","status","category","created_at","owner_changes"]
df["created_at"]=pd.to_datetime(df["created_at"],errors="coerce")
valid=df.dropna(subset=required)
valid=valid[
    valid["id"].astype(str).str.strip().ne("")&
    valid["source"].isin(["salesforce","jira","servicenow"])&
    valid["status"].isin(["open","closed"])&
    valid["category"].astype(str).str.strip().ne("")&
    (valid["owner_changes"]>=0)
]
print("================================")
print("Q21 - VALIDATION")
print("================================")
print("Valid records:",len(valid))
print("Rejected records:",len(df)-len(valid))
unique=valid.drop_duplicates(subset=["source","id"])
print("\n================================")
print("Q22 - DEDUPLICATION")
print("================================")
print("Unique records:",len(unique))
print("Duplicates removed:",len(valid)-len(unique))
print("\n================================")
print("Q23 - SUMMARY")
print("================================")
print("Total:",len(unique))
print("\nBy Status:")
print(unique["status"].value_counts())
print("\nBy Source:")
print(unique["source"].value_counts())
print("\nBy Category:")
print(unique["category"].value_counts())
reference=pd.Timestamp("2026-09-30")
unique=unique.copy()
unique["age"]=(reference-unique["created_at"]).dt.days
aging=unique[
    (unique["status"]=="open")&
    (unique["age"]>7)
]
handoff=unique[
    unique["owner_changes"]>3
]
print("\n================================")
print("Q24 - FINDINGS")
print("================================")
print("\nAging records:")
print(aging[["source","id","age"]])
print("\nHandoff records:")
print(handoff[["source","id","owner_changes"]])