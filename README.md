# Workload Identity GCP

This repo show how you can configure and start use Workload Identity provider from ANNA Money GCP

```yaml
- name: "Auth in GCP"
  id: "auth"
  uses: "google-github-actions/auth@v0"
  with:
    token_format: "access_token"
    workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER_NAME }}
    service_account: ${{ secrets.GCP_WORKLOAD_IDENTITY_SA_EMAIL }}
    access_token_lifetime: '900s' # Default 3600s

- name: "Docker login"
  run: |
    echo '${{ steps.auth.outputs.access_token }}' | docker login -u oauth2accesstoken --password-stdin https://eu.gcr.io
```

**secrets.GCP_WORKLOAD_IDENTITY_PROVIDER_NAME** and **secrets.GCP_WORKLOAD_IDENTITY_SA_EMAIL** — already exist at the organization level and you can start using them.
