# Команды для работы с storage в minikube

## Ephemeral storage

Создание configmap из файла:

```bash
kubectl create configmap index-configmap --from-file nginx_index.html
```

Создание деплоймента с volume types configMap (folder mount) and emptyDir:

```bash
kubectl apply -f 10-nginx-mount-folder.yaml
```

- Зайдите в под и убедитесь, что в папке /usr/share/nginx/html/ только один файл - index.html
- Содержимое файла взято из configmap
- Создайте файлы в папке /nginx_cache внутри пода, удалите под, зайдите в пересозданный под, папка /nginx_cache будет пустой

Создание деплоймента с volume types configMap (file mount) and emptyDir:

```bash
kubectl apply -f 11-nginx-mount-file.yaml
```

- Зайдите в под и убедитесь, что в папке /usr/share/nginx/html/ два файла - index.html (из configmap) и 50x.html

## Persistent storage

Монтирование папки на локальном компьютере в minikube:

```bash
minikube mount <путь к локальной папке>:/mnt_data
```

Создание persistent volume (type hostPath):

```bash
kubectl apply -f 20-pv.yaml
```

Создание persistent volume claim:

```bash
kubectl apply -f 21-pvc.yaml
```

Создание пода с persistent volume:

```bash
kubectl apply -f 22-pod.yaml
```

- В подключенной папке появится файл date.txt
- При каждом запуске пода в файле будет появляться новая строчка с датой и временем
