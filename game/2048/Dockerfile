FROM openeuler/openeuler:24.03-lts as builder
RUN dnf -y install git make gcc-c++
RUN git clone https://github.com/mevdschee/2048.c.git /tmp/2048 && \
    cd /tmp/2048 && make -j $(nproc)

FROM openeuler/distroless:base-oe2203lts
COPY --from=builder /tmp/2048/2048 /usr/local/bin
CMD ["/usr/local/bin/2048"]
