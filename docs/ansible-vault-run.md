`ansible-vault-run` will decrypt a vault and run a script with the variables exported as environment variables
    echo "Decrypts an ansible-vault and runs script with the contents as environment variables"
```bash
ansible-vault-run vault "echo \$password"
```
