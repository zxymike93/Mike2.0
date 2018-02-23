#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <syslog.h>
#include <string.h>


void mylog()
{
    int fd;
    char buf[] = "hello world\n";
    int n = 13;

    fd = creat("log.txt", 0666);
    write(fd, buf, n);
}


int main()
{
    pid_t pid, sid;

    // fork off parent process
    pid = fork();

    // fail: -1
    if (pid < 0)
        exit(EXIT_FAILURE);

    // success: non-zero
    if (pid > 0)
        exit(EXIT_SUCCESS);

    // file mode mask
    umask(0);

    // open logs

    // create sid for child process
    sid = setsid();
    if (sid < 0)
        exit(EXIT_FAILURE);

    // change directory to guarantee
    if ((chdir("/")) < 0)
        mylog();
        exit(EXIT_FAILURE);

    // daemon cannot print on terminal
    // close file descriptor
    close(STDIN_FILENO);
    close(STDOUT_FILENO);
    close(STDERR_FILENO);


    // code down here
    while (1) {
        sleep(30);
    }
    exit(EXIT_SUCCESS);
}
