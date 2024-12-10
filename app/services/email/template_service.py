from pathlib import Path
from typing import Dict

from jinja2 import Environment, FileSystemLoader


class EmailTemplateService:

    template_dir: str = (
        Path(__file__).parent.parent.parent / "services/email/templates/"
    )
    payment_confirmation_template = "payment_confirmation.html"

    def __init__(self):
        """
        Initialize the email template engine.

        Args:
            template_dir (str): Directory containing email templates.
        """

        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def render_template(self, template_name: str, context: Dict[str, str]) -> str:
        """
        Render the email template with the given context.

        Args:
            template_name (str): Name of the template file.
            context (Dict[str, str]): Variables to substitute in the template.

        Returns:
            str: Rendered template as a string.
        """
        try:
            template = self.env.get_template(template_name)
            return template.render(context)
        except Exception as e:
            print(f"Failed to render template: {e}")
            raise


template_service = EmailTemplateService()
