/***************************************************************************
**
** Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
** All rights reserved.
** Contact: Nokia Corporation (directui@nokia.com)
**
** This file is part of applauncherd
**
** If you have questions regarding the use of this file, please contact
** Nokia at directui@nokia.com.
**
** This library is free software; you can redistribute it and/or
** modify it under the terms of the GNU Lesser General Public
** License version 2.1 as published by the Free Software Foundation
** and appearing in the file LICENSE.LGPL included in the packaging
** of this file.
**
****************************************************************************/

#include <MApplication>
#include <MApplicationPage>
#include <MApplicationWindow>
#include <QDebug>
#include <MExport>
#include <MButton>
#include <MLabel>
#include <QString>
#include <MSlider>
#include <MLayout>
#include <MLinearLayoutPolicy>
#include <QFile>
#include <sys/time.h>
#include <exception>

#ifdef HAVE_MCOMPONENTCACHE
#include <mcomponentcache.h>
#endif

QString log_file = "/tmp/fala_hello.log";

void FANGORNLOG(const char *s)
{
    QFile f(log_file);
    f.open(QIODevice::Append);
    f.write(s, qstrlen(s));
    f.write("\n", 1);
    f.close();
}

void timestamp(const char *s)
{
    timeval tim;
    char msg[80];
    gettimeofday(&tim, NULL);
    snprintf(msg, 80, "%d%03d %s", 
             static_cast<int>(tim.tv_sec), static_cast<int>(tim.tv_usec)/1000, s);
    FANGORNLOG(msg);
}

void timestamp(const QString& s)
{
    QByteArray ba = s.toLocal8Bit();
    char *p = new char[ba.size() + 1];
    strcpy(p, ba.data());
    timestamp(p);
}

M_EXPORT int main(int argc, char ** argv)
{
    MApplication *app;
    try
    {

#ifdef HAVE_MCOMPONENTCACHE
        app = MComponentCache::mApplication(argc, argv);
        MApplicationWindow *window = NULL;

        bool bWindowNotFromCache = false;
        const QString sWindowNotFromCache = "window-not-from-cache";

        for (int i = 1; i < argc; i++) {
            QString sArg = QString(argv[i]);
            if (sArg.contains(sWindowNotFromCache,Qt::CaseInsensitive)) {
		bWindowNotFromCache = true;
		break;
            }
        }
	
        if (bWindowNotFromCache) {
            window = new MApplicationWindow();
            timestamp("MApplicationWindow NOT from cache");
        } else {
            window = MComponentCache::mApplicationWindow();
            timestamp("MApplicationWindow from cache");
        }
#else
        app = new MApplication(argc, argv);
        MApplicationWindow *window = new MApplicationWindow;
#endif

        timestamp(QString("applicationDirPath: ").append(QApplication::applicationDirPath()));
        timestamp(QString("applicationFilePath: ").append(QApplication::applicationFilePath()));

        MApplicationPage *mainPage = new MApplicationPage;
        mainPage->setTitle("Hello World! (Now supports Launcher)");
        mainPage->centralWidget()->setObjectName("centralWidget");

        MLayout *layout = new MLayout(mainPage->centralWidget());
        MLinearLayoutPolicy *linearPolicy = new MLinearLayoutPolicy(layout,
                                                                    Qt::Vertical);

        linearPolicy->addItem(new MLabel("I'm a label"));
        linearPolicy->addItem(new MButton("Click me!"));
        linearPolicy->addItem(new MSlider);

        window->show();

        const char *foobar = "foo!";
        for (int i = 0; i < argc; ++i)
        {
            if (QString(argv[i]) == "-segfault")
            {
                const_cast<char *>(foobar)[3] = 'z';
            }
        }

        // Explicitly state where to appear, just to be sure :-)
        mainPage->appear(window);

    }
    catch(std::exception& e)
    {
        return -1;
    }
    _exit(app->exec());
}
