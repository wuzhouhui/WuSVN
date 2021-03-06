#ifndef SVN_COLOR_H
#define SVN_COLOR_H

#define SVN_USE_COLOR_MAGIC   0x8a3f
#define SVN_COLOR_RED          "\033[31m"
#define SVN_COLOR_GREEN        "\033[32m"
#define SVN_COLOR_BLUE         "\033[34m"
#define SVN_COLOR_YELLOW       "\033[33m"
#define SVN_COLOR_MAGENTA      "\033[35m"
#define SVN_COLOR_CYAN         "\033[36m"
#define SVN_COLOR_RESET        "\033[m"
#define SVN_COLOR_BG_RED       "\033[41m"

extern svn_boolean_t dont_use_color;
extern int tty_fileno;

#endif /* SVN_COLOR_H */
