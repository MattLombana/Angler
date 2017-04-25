
# Angler

Angler: A Simple Web Hook For Saving And Viewing URL Requests

## Installing Angler

```shell
virtualenv -p python3 <virtualenv_name>
cd <virtualenv_name>
. bin/activate
git clone https://github.com/MattLombana/Angler
cd Angler
pip3 install -Ur requirements.txt
```

## Configuring Angler

You can edit the port that Angler runs on by editing it in `run.py`

## Running Angler

```shell
./run.py
```

## Using Angler

View all requests by visiting either `/` or `/release`
Create a request by visiting `/catch` with something added to the end of `catch`
For example, to log ?foo=bar, I would visit `localhost:5000/catch?foo=bar`
