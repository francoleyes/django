# Python Dev Challenge - Backend con Django y DRF

## Introducción
Este proyecto es parte del desafío de desarrollo en Python para la construcción de un bot de toma de pedidos para la empresa Heladerías Frozen SRL. El objetivo de este proyecto es desarrollar las funciones auxiliares que permitirán al bot interactuar en la conversación y realizar las operaciones necesarias para la creación de órdenes de compra.

## URL BACKEND
https://django-server-production-9787.up.railway.app/admin
- usuario: hfrozen
- password: hfrozen123
![image](https://github.com/francoleyes/heladerias_frozen_backend/assets/85895403/08ce0f0c-f8fd-4552-8f00-b6f002b56869)

## Cosas extras y dinámicas agregadas a las consignas
- Mensajes de bienvenida: Se puede crear un mensaje personalizado para cada rango de temperatura. Tiene validaciones para no pisarse entre las temperatuas y devuelve el mensaje de bienvenida según la temperatura obtenida de la API del pdf.
![image](https://github.com/francoleyes/heladerias_frozen_backend/assets/85895403/30f7622a-6321-4759-aea0-c41def9e2c6d)

- Código de descuento: Se pueden crear cualquier más códigos de descuento y se le puede configurar la cantidad de usos y el descuento que tienen en la compra.
![image](https://github.com/francoleyes/heladerias_frozen_backend/assets/85895403/b92f9092-5ddb-4b04-8719-4b864fb9cc3b)

- Productos: Se pueden crear los productos a mostrar como tambien su precio, stock y la imagen que se va a mostrar en el frontend.
![image](https://github.com/francoleyes/heladerias_frozen_backend/assets/85895403/5571bd1e-037d-4c52-b94a-2d74a35abf95)

- Orden y Orden de compra: en la orden aparece el nombre del comprador (que viene desde el frontend) y el total de la compra con el descuento aplicado si corresponde. Esta orden esta asociada a la orden de compra la cual contiene distintos registros que contienen el producto y la cantidad del mismo.
![image](https://github.com/francoleyes/heladerias_frozen_backend/assets/85895403/07cc4396-a5bd-4f9d-b24d-7d1dc7b4ad47)
![image](https://github.com/francoleyes/heladerias_frozen_backend/assets/85895403/fcd140cb-67a4-4b5c-94d0-a03c92255ee3)


## Endpoints

El proyecto backend expone los siguientes endpoints:

- `/api/create-order/`: Permite crear una nueva orden de compra.
- `/api/products/`: Permite obtener la lista de productos disponibles.
- `/api/discount/validate/`: Permite obtener la validación del código de descuento.
- `/api/welcome-message/`: Permite obtener el mensaje de bienvenida según la temperatura obtenida en la API del pdf de ejercicios.

La documentación se encuentra en: https://django-server-production-9787.up.railway.app/docs/

