from app.services.github_service import (
    get_repository_files,
    get_file_content
)

from app.services.chunking_service import (
    chunk_python_code
)


repo_url = "https://github.com/fastapi/fastapi"


files = get_repository_files(repo_url)

print("TOTAL FILES:")
print(len(files))


python_files = [
    file for file in files
    if file.endswith(".py")
]

first_file = python_files[0]

print("\nFIRST FILE:")
print(first_file)


content = get_file_content(repo_url, first_file)

print("\nFETCHED CONTENT:")
print(content[:500])


chunks = chunk_python_code(content)

print("\nTOTAL CHUNKS:")
print(len(chunks))


for chunk in chunks[:3]:

    print("\n-------------------")

    print("FUNCTION NAME:")
    print(chunk["name"])

    print("\nLINES:")
    print(
        chunk["start_line"],
        "to",
        chunk["end_line"]
    )

    print("\nCODE:")
    print(chunk["code"][:300])