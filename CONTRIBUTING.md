# 🤝 Contributing to OMNIS2

Thank you for your interest in contributing to OMNIS2! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)

## 📜 Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please be respectful and constructive in all interactions. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details.

## 🎯 How Can I Contribute?

### Reporting Bugs

- Use the [GitHub issue tracker](https://github.com/Baver1022/omnis2-pi-analysis/issues)
- Include a clear title and description
- Provide steps to reproduce the bug
- Include system information (OS, Python version, etc.)

### Suggesting Enhancements

- Open an issue with the `enhancement` label
- Clearly describe the feature and its use case
- Explain why this enhancement would be useful

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Test your changes** thoroughly
5. **Commit your changes** (`git commit -m 'Add amazing feature'`)
6. **Push to the branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

## 🛠️ Development Setup

### Prerequisites

- Python 3.8+
- Git
- CUDA-capable GPU (for GPU acceleration)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/omnis2-pi-analysis.git
cd omnis2-pi-analysis

# Checkout OMNIS2 branch
git checkout OMNIS2

# Install dependencies
cd Program
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # If available
```

## 🔄 Pull Request Process

1. **Update documentation** if you've changed functionality
2. **Add tests** for new features (if applicable)
3. **Ensure all tests pass**
4. **Update CHANGELOG.md** with your changes
5. **Request review** from maintainers

### PR Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] All tests pass

## 📝 Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions focused and single-purpose

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in imperative mood (e.g., "Add", "Fix", "Update")
- Reference issue numbers when applicable

Example:
```
Add LSTM neural network for pattern prediction

- Implemented LSTM model for Pi digit sequence analysis
- Added training and evaluation scripts
- Updated documentation with usage examples

Fixes #123
```

## 🧪 Testing

Before submitting a PR, ensure:

- All existing tests pass
- New code is covered by tests
- Code runs without errors
- No linting errors

## 📚 Documentation

- Update README.md if you add new features
- Add docstrings to new functions/classes
- Update relevant documentation files

## ❓ Questions?

Feel free to open an issue or start a discussion if you have questions about contributing!

---

Thank you for contributing to OMNIS2! 🎉

