FROM openvino/ubuntu20_data_runtime:2021.4

ENV DEVICE=CPU
WORKDIR /home/openvino/workdir
ADD . /home/openvino/workdir/

# Support Arbitrary User IDs - OCP Secure Guidelines
# USER root
# RUN chgrp -R 0 /home/openvino && \
#     chmod -R g=u /home/openvino
# USER openvino

ENTRYPOINT [ "/home/openvino/workdir/run.sh" ]