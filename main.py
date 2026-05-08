from blockchain.blockchain import Blockchain
from utils.hash_utils import hash_document


# ---------------- VERIFY DOCUMENT ----------------
def verify_document(file_path, blockchain):
    current_hash = hash_document(file_path)

    for block in blockchain.chain:
        if block.document_hash == current_hash:
            print("\ Document is VERIFIED")
            print("Timestamp:", block.timestamp)
            return

    print("\n Document NOT found or has been modified")


# ---------------- VALIDATE BLOCKCHAIN + FILE ----------------
def validate_document_and_blockchain(file_path, blockchain):
    current_hash = hash_document(file_path)

    # Step 1 → Check blockchain structure
    if not blockchain.is_chain_valid():
        print("\n Blockchain structure has been tampered!")
        return

    # Step 2 → Check file hash inside blockchain
    for block in blockchain.chain:
        if block.document_hash == current_hash:
            print("\n Blockchain is valid")
            print(" Document is authentic")
            print("Timestamp:", block.timestamp)
            return

    print("\n Validation failed: integrity check unsuccessful.")


def main():
    blockchain = Blockchain()

    while True:
        print("\n===== Document Timestamping System =====")
        print("1. Add Document")
        print("2. Verify Document")
        print("3. Show Blockchain")
        print("4. Validate Blockchain")
        print("5. Exit")

        choice = input("Enter choice: ")

        # ADD DOCUMENT
        if choice == "1":
            path = input("Enter file path: ").strip().strip('"')

            try:
                doc_hash = hash_document(path)
                blockchain.add_block(doc_hash)

                print("\n✅ Document added successfully!")
                print("Hash:", doc_hash)

            except:
                print("\nFile not found!")

        # VERIFY DOCUMENT
        elif choice == "2":
            path = input("Enter file path: ").strip().strip('"')

            try:
                verify_document(path, blockchain)

            except:
                print("\n File not found!")

        # SHOW BLOCKCHAIN
        elif choice == "3":
            blockchain.display_chain()

        # VALIDATE BLOCKCHAIN
        elif choice == "4":
            path = input("Enter file path to validate: ").strip().strip('"')

            try:
                validate_document_and_blockchain(path, blockchain)

            except:
                print("\n File not found!")

        # EXIT
        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("\n Invalid choice")


if __name__ == "__main__":
    main()