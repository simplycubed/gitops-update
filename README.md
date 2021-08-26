# gitops-update

Github action that updates a single key in other github repository.

## Example:

You have a deployment.yaml file in a `myorg/app-env` repository that has below content:

Add this to github acion:

```text
- name: GitOps Update
    uses: simplycubed/gitops-update@master
    with:
      filename: "path/to/deployment.yaml"
      key: "image"
      value: '${{ secrets.REGISTRY_LOGIN_SERVER }}/sampleapp:${{ github.sha }}'
      github-deploy-key: ${{ secrets.GITOPS_SSH_PRIVATE_KEY }}
      github-org-and-repo:  "myorg/app-env"
```

