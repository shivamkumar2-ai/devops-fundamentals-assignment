from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
Q1 = ROOT / "q1-ec2-nginx"


class WebsiteTests(unittest.TestCase):
    def test_website_files_exist(self):
        for name in ("index.html", "styles.css", "app.js"):
            self.assertTrue((WEBSITE / name).is_file(), f"Missing {name}")

    def test_website_shows_required_content(self):
        html = (WEBSITE / "index.html").read_text(encoding="utf-8")
        required = (
            "DevOps Training",
            "CI/CD Deployment Successful",
            "Version:",
            "2.0",
            "Deployed automatically using GitHub Actions",
        )
        for snippet in required:
            self.assertIn(snippet, html)

    def test_q1_page_shows_required_content(self):
        html = (Q1 / "index.html").read_text(encoding="utf-8")
        required = (
            "DevOps Training",
            "Application deployed successfully!",
            "Server: AWS EC2",
            "Web Server: NGINX",
        )
        for snippet in required:
            self.assertIn(snippet, html)


if __name__ == "__main__":
    unittest.main()
