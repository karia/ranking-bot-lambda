# ranking-bot

## require

* Docker
* aws-sam-cli
* python3.8
* pip

## deploy

./build_run.sh

upload `deploy_package.zip` to Lambda.

## execute in local

```
cp template.yaml.sample template.yaml
code template.yaml

cp event.json.sample event.json
code event.json
```

After edit & save, and exec:

```
sam local invoke --event event.json
```
