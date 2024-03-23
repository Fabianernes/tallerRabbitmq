#!/usr/bin/env ruby

require 'bunny'

# Obtener las credenciales de las variables de entorno
user = ENV['RABBITMQ_USER'] || 'user'
password = ENV['RABBITMQ_PASS'] || 'password'

# Establecer la conexión con RabbitMQ
connection = Bunny.new(username: user, password: password, host: 'rabbitmq')
connection.start

channel = connection.create_channel

# Declara un intercambio llamado "logs" de tipo "fanout"
exchange = channel.fanout('logs')

# Obtén el mensaje de los argumentos de la línea de comandos o usa un mensaje predeterminado
message = ARGV.empty? ? 'Esta es la prueba de que me merezco un 5 en el taller' : ARGV.join(' ')

# Publica el mensaje en el intercambio "logs" sin especificar una clave de enrutamiento (fanout)
exchange.publish(message)
puts " [x] Enviado #{message}"

connection.close
