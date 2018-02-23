# include <stdio.h>

/* 指向序列的指针，序列中的元素为非负整数 */
typedef unsigned char *byte_pointer;

/* 以16进制打印指针的每一位，每一位至少对应两位的16进制 */
void show_bytes(byte_pointer start, int len)
{
    int i;
    for (i = 0; i < len; i++) {
        printf(" %.2x", start[i]);
    }
    printf("\n");
}

/**
 * 参数 x 的指针 &x 类型为 x 的类型
 * 但byte_pointer 强制转换它为 unsigned char
 */
void show_int(int x)
{
    show_bytes((byte_pointer) &x, sizeof(int));
}

void show_float(float x)
{
    show_bytes((byte_pointer) &x, sizeof(float));
}

void show_pointer(void *x)
{
    show_bytes((byte_pointer) &x, sizeof(void *));
}

void test_show_bytes(int val)
{
    int ival = val;
    float fval = (float) ival;
    int *pval = &ival;
    show_int(ival);
    show_float(fval);
    show_point(pval);
}

void show_simple_a()
{
    int val = 0x87654321;
    byte_pointer valp = (byte_pointer) &val;
    show_bytes(valp, 1);
    show_bytes(valp, 2);
    show_bytes(valp, 3);
}

void show_simple_b()
{
    int val = 0x12345678;
    byte_pointer valp = (byte_pointer) &val;
    show_bytes(valp, 1);
    show_bytes(valp, 2);
    show_bytes(valp, 3);
}

void show_string_ueg()
{
    const char *s = "ABCDEF";
    show_bytes((byte_pointer) s, strlen(s));
}

void show_string_leg()
{
    const char *s = "abcdef";
    show_bytes((byte_pointer) s, strlen(s));
}

int main(int argc, char *argv[])
{
    int val = 12345;

    if (argc > 1) {
        val = strtol(argv[1], NULL, 0);
        test_show_bytes(val);
    } else {
        show_towcomp();
        show_simple_a();
        show_simple_b();
        float_eg();
        string_ueg();
        string_leg();
    }
    return 0;
}
