FROM python:3.9-slim

WORKDIR /code

RUN pip install \
	torch==2.0.1+cpu \
	torchvision==0.15.2+cpu \
	--extra-index-url https://download.pytorch.org/whl/cpu \
	&& rm -rf /root/.cache/pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./model_server_src.py /code/

CMD ["uvicorn", "model_server_src:app", "--host", "0.0.0.0", "--port", "80"]