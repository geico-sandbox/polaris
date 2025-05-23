#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

FROM ubuntu:24.04 AS hugo

ENV LANGUAGE='en_US:en'

RUN apt-get update
RUN apt-get install --yes golang hugo asciidoctor npm curl
RUN apt-get clean
# http-server is used when building the static site to manually check it locally
# (via `site/bin/create-static-site.sh --local` at http://localhost:8080/)
RUN npm install --global http-server

# these dependencies are needed to build the static site
#RUN npm install --global autoprefixer postcss postcss-cli http-server

RUN mkdir /polaris
RUN mkdir /polaris/site
RUN mkdir /polaris/site/resources

COPY _run_in_docker.sh /hugo/run

EXPOSE 1313
EXPOSE 8080

ENTRYPOINT ["/hugo/run"]
