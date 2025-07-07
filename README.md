# **Examen Final Numero 1**
**Alumno:** `Chowdhury Gomez, Junal`
**Codigo:** `20200092K`

![](https://github.com/JunalChowdhuryG/Examen-Final-Chowdhury/actions/workflows/pipeline.yml/badge.svg)

## **1. Modulos de Terraform**

* Cree el  `provider.tf` [iac/provider.tf](iac/provider.tf) el cual define los provider y el backend de manera local siguiendo el patron **Singleton**

* Cree el `main.tf` [iac/main.tf](iac/main.tf) el cual define los recurso agrupados en modulos reutilizables como network, subnet, iam siguiendo el patron **Composite**
    - Tambien se crea instancias de recursos de computo siguiendo el ppatron **Factory**

## **2. Testing de infraestructura**
* En el pipeline [.github/workflows/pipeline.yml](.github/workflows/pipeline.yml) solo hice el analisis estatico mediante:

```yml
- name: Run Tfsec
  uses: aquasecurity/tfsec-action@v1.0.0
```

## **3. Contenerizacion Docker y Docker Compose**
* Cree los 2 microservicions:
    - Manejo de usuario: [Service-usuario](service-usuario/)
    - Gestion de productos: [Service-producto](service-producto/)
* Cada uno con su archivo Dockerfile:
    - [service-producto/Dockerfile](service-producto/Dockerfile)
    - [service-usuario](service-usuario/Dockerfile)
* Ambos dockerfile bajo un enfoque **multi-stage build** con fases separadas:
**build** y **runtime**
* Con volummenes para persistencia de datos


**"Declaro que esta entrega fue realizada sin ayuda externa ni herramientas automaticas"**

