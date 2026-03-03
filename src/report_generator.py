import json
import os


class ReportGenerator:
    """
    Handles exporting scan results to JSON format.
    """

    def __init__(self, output_directory="output/sample_output"):
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)

    def save_to_json(self, data, filename="scan_result.json"):
        file_path = os.path.join(self.output_directory, filename)

        try:
            with open(file_path, "w") as json_file:
                json.dump(data, json_file, indent=4)

            print(f"\n[+] Results saved to {file_path}")

        except Exception as e:
            print(f"[!] Failed to save report: {e}")