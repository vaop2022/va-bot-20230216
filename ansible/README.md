# Ansible

Here we can provison a DigitalOcean droplet and deploy this app to it

## Initial run

grab the roles

```shell
ansible-galaxy install -r requirements.yml
```

prep for ssh key into provision: 

make sure to have it available for ssh agent 

```shell
ssh-add ~/.ssh/id_telegram_bots_do
```

get an id of pub key uploaded to do (the `~/.ssh/id_telegram_bots_do.pub` above):

```shell
 curl --silent "https://api.digitalocean.com/v2/account/keys?per_page=999" -H "Authorization: Bearer $DO_API_TOKEN" | python -m json.tool
```

there is a seperate github key to patch through for cloning the private repo.

```
# in ~/.ssh/config
Host 178.128.229.237
  ForwardAgent yes
```

where that is the ip above is the provisioned DO droplet

## Ansible roles


### Digital Ocean (provisioner)

For digital ocean, you need to have the following env variable set: 

```shell
export DO_API_TOKEN=
```

## Roles

### Postgresql

https://github.com/geerlingguy/ansible-role-postgresql

```yml
- hosts: database
  roles:
    - role: geerlingguy.postgresql
      become: yes
```