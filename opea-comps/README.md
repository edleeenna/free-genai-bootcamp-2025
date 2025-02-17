# Ollama on Docker

## Prequistites
- Docker installed

## Running Ollama Third-Party Service

### Choosing a model

You can get hte model_id that ollama will alunch from the [Ollama Library](https://ollama.com/library)

e.g. https://ollama.com/library/llama3.2

### Getting the host IP

#### MacOS

Get your IP address

```sh
ipconfig getifaddr en0
```

Or you can try this way `=$(hostname -I | awk '{print $1}')`

export LLM_ENDPOINT_PORT=8008
export no_proxy=localhost,127.0.0.1
export LLM_MODEL_ID=llama3.2:1b
export host_ip=192.168.0.178
docker-compose up

### Ollama API

Once the Ollama server is running we can make API calls to the ollama API

https://github.com/ollama/ollama/blob/main/docs/api.md

### Pull a model

``` sh
curl http://localhost:8008/api/pull -d '{
  "model": "llama3.2:1b"
}'
```

### Generate a request
```sh
curl http://localhost:8008/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "Why is the sky blue?"
}'
```

### Technical Uncertainty

Q Does bridge mode mean we can only access Ollama API with another model in the docker compose?

A No, the host machine will be able to access it

Q Which port is being mapped 8008 -> 1234321

In this case 8008 is the port that the host machine will access. The other port is the guet post, the port of the service inside the container

Q If we pass the LLM_MODEL_ID to the ollama server will it download the model on start

A It does not appear so. The ollama CLI might be running multiple APIs so you need to call the / pull api before trying to generate text

Q Will the model be downloaded in the container? and does that mean the model will delete when the model stops running?

A the model will download into the container and vanish when the container stop running. You need to mount a local drive and there is probably more work to be done.