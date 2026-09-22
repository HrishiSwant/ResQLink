# ResQLink Continuous Deployment & Delivery

## 1. Continuous Delivery

Continuous Delivery is a software development practice where application changes are automatically built, tested, and prepared for release.

The application is kept in a deployable state.

ResQLink implements Continuous Delivery using:

- GitHub
- GitHub Actions
- Automated backend tests
- Frontend build
- CI pipeline
- Pull requests
- Protected branches
- Vercel deployment
- Render deployment

Pipeline:

```text
Code
  ↓
Build
  ↓
Test
  ↓
Package
  ↓
Ready for Deployment
