FROM centos:7
RUN yum -y install epel-release
RUN yum -y update
RUN yum -y install nginx
echo "this is test for docker pipeline" > /usr/share/nginx/html/index.html
EXPOSE 80/tcp
CMD ["nginx", "-g daemon off;"]
