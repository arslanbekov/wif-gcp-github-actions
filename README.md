# Workload Identity GCP

This repo show how you can configure and start use Workload Identity provider from ANNA Money GCP

```yaml
name: "Workload name"
jobs:
  run:
    name: "Example Job name"
    permissions:
      id-token: write
      contents: read
    runs-on: ubuntu-latest
    steps:
      - name: "Auth in GCP"
        id: auth
        uses: "google-github-actions/auth@v0"
        with:
          token_format: "access_token"
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER_NAME }}
          service_account: ${{ secrets.GCP_WORKLOAD_IDENTITY_SA_EMAIL }}
          access_token_lifetime: "900s" # Default 3600s

      - name: "Docker login"
        run: |
          echo '${{ steps.auth.outputs.access_token }}' | docker login -u oauth2accesstoken --password-stdin https://eu.gcr.io
```

**Important permissions:**

```yaml
permissions:
  id-token: write
  contents: read
```

Also `GCP_WORKLOAD_IDENTITY_PROVIDER_NAME` and `GCP_WORKLOAD_IDENTITY_SA_EMAIL` secrets already exist at the organization level and you can start using them.

## Links

1. [GCP GHA Keyless description](https://cloud.google.com/blog/products/identity-security/enabling-keyless-authentication-from-github-actions)
2. [GCP WIP documentation](https://cloud.google.com/iam/docs/configuring-workload-identity-federation)
3. [ANNA-Money terraform WIP](https://github.com/anna-money/anna-terraform/tree/master/gcp-workload-identity)
4. [GHA auth in gcp action](https://github.com/google-github-actions/auth)
