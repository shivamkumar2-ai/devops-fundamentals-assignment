const versionEl = document.getElementById("app-version");
const deployedAtEl = document.getElementById("deployed-at");

const version = versionEl ? versionEl.textContent.trim() : "2.0";
const deployedAt = new Date().toISOString();

if (deployedAtEl) {
  deployedAtEl.textContent = `Version ${version} is live. Page loaded at ${deployedAt}.`;
}
