# NYU OFFSEC

You can use this attachment to build the same docker container as the server end.

- You can find the glibc on the container: `/lib/x86_64-linux-gnu/libc.so.6`
- If you can run the container and solve the challenge but can't solve the remote one, please DM TA@Xiang
- The challenge is running on localhost port 9999.
- Please stop the container when you don't need it or other people can attack the server.

Usage:
```bash
docker build -t nyuoffsec:chal .
docker run -p 9999:9999 nyuoffsec:chal
```
