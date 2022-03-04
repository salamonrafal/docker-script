# Simple Script Management Service Dockerized  

## Description 

This script created for easily manage build and run PHP service. For that  used docker image and docker compose. This is template for final implementation. If you would like to use it  you need to adjust script functionalities to your requirements.

## Parameters

### Schema

```shell
python run.py [--command|-c build|docker-image|docker-compose|docker-container|docker-container|clean]
              [--image_name|-i *]
              [--docker_file|-d *]
              [--version|-vd *]
              [--action|-a start|stop|destroy]
              [--environment|-e production|development]
```

### Descriptions of arguments

| **Long Name**                     | **Short Name**          | **Description**                                                                                                                                                                                                                                                                                                                |
|-----------------------------------|-------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <pre>--command [string]</pre>     | <pre>-c [string]</pre>  | Type of command to run. List of available types: <pre>build, docker-image, docker-compose, docker-container, clean</pre>                                                                                                                                                                                                       |
| <pre>--image_name [string]</pre>  | <pre>-i [string]</pre>  | Name of docker image. It **required** when you **build** image after that this information save to cache file. When you run container you do not need repeat this information, but you always overwrite cached data.                                                                                                           |
| <pre>--docker_file [string]</pre> | <pre>-d [string]</pre>  | Set custom name of Dockerfile. Default is **Dockerfile**                                                                                                                                                                                                                                                                       |
| <pre>--version [string]</pre>     | <pre>-vd [string]</pre> | Set version of docker image. You can omit this argument. Similar behavior too `--image_name` argument. When you run **build** image after that this information save to cache file. When you run container you do not need repeat this information, but you always overwrite cached data.                                      |
| <pre>--action [string]</pre>      | <pre>-a [string]</pre>  | This parameter **required** when you run `docker-container`. List of available action types: <pre>start, stop, destroy</pre>                                                                                                                                                                                                   |
| <pre>--environment [string]</pre> | <pre>-e [string]</pre>  | This parameter pointing for which environment you would like build or run service. It sets proper shell variable which contains this information. When you use build image or compose commands then it uses proper files specified for selected environment. List of available environments <pre>production, development</pre> |

### Rules

#### command: build

```shell
python run.py --command build --image_name :string --environment production|development [--version string] [--docker_file string]
```

**Required**
* `--image_name`
* `--environment`

**Optional**
* `--version`
* `--docker_file`


#### command: docker-image

```shell
python run.py --command docker-image [--image_name :string] [--environment production|development] [--version :string] [--docker_file :string]
```

**Optional**
* `--image_name`
* `--environment`
* `--version`
* `--docker_file`

#### command: docker-compose

```shell
python run.py --command docker-compose [--image_name :string] [--environment production|development] [--version :string] 
```
#### command: docker-container
```shell
python run.py --command docker-container --action start|stop|destroy [--image_name :string] [--environment production|development] [--version :string]
```

**Required**
* `--action`

**Optional**
* `--version`
* `--environment`

#### command: clean

```shell
python run.py --command docker-clean
```