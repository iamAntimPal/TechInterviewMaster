When you **create a pull request (PR)** on GitHub, you can manage **Issues** (like linking or closing them) **from the PR description or comment section** using special keywords. Here's how you can do it:

---

### ✅ **To link and close issues from a Pull Request**

#### 🔗 Use keywords in your PR description or comments:

**Syntax:**
```markdown
Fixes #123
Closes #456
Resolves #789
```

This tells GitHub to **automatically close** those issues when the PR is merged.

---

### 💡 Example Pull Request Description

```markdown
## What does this PR do?
- Fixes bug in user login
- Updates UI on dashboard

## Linked Issues
Fixes #12
Closes #15
```

When the PR is merged:
- Issue #12 and #15 will automatically be closed.
- GitHub will show a link to the PR under those issues too.

---

### 🛠 Supported Keywords

You can use any of the following before an issue number:

| Action      | Keywords                     |
|-------------|------------------------------|
| 🔒 Close     | `close`, `closes`, `closed`  |
| ✅ Fix       | `fix`, `fixes`, `fixed`      |
| 🧩 Resolve   | `resolve`, `resolves`, `resolved` |

---

### 🧪 Bonus: Multiple Issues

You can reference **multiple issues** like this:

```markdown
Fixes #101, resolves #202, closes #303
```

---

### 📌 Note:
- The `#` number must refer to **issues in the same repository**.
- The closing action only happens when the PR is **merged into the default branch** (usually `main` or `master`).
