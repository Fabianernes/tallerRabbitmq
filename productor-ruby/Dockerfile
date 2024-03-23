# Usa una imagen base con Ruby preinstalado
FROM ruby:latest

# Copia el script al contenedor
COPY productor-ruby.rb /usr/src/app/productor-ruby.rb

# Instala la gema Bunny para la comunicación con RabbitMQ
RUN gem install bunny

# Establece el directorio de trabajo
WORKDIR /usr/src/app

ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=password

# Ejecuta el script cuando se inicie el contenedor
CMD ["ruby", "./productor-ruby.rb"]
