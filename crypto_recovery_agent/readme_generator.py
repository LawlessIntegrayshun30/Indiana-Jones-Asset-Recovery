## readme_generator.py
import json
from typing import Dict

class ReadmeGenerator:
    """
    A class responsible for generating a README file for the project.
    """
    
    def generate_readme(self, content: Dict[str, str]) -> str:
        """
        Generate the README content from a dictionary of sections.
        
        :param content: A dictionary where keys are section titles and values are the section contents.
        :return: A string representing the formatted README content.
        """
        readme_content = []
        for section_title, section_content in content.items():
            readme_content.append(f"## {section_title}\n{section_content}\n")
        
        return "\n".join(readme_content)

# Example usage:
# if __name__ == "__main__":
#     generator = ReadmeGenerator()
#     sections = {
#         "Introduction": "This project is about...",
#         "Installation": "To install the dependencies...",
#         "Usage": "To use this application...",
#     }
#     readme = generator.generate_readme(sections)
#     print(readme)
