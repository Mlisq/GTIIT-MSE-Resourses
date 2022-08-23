#ifndef CONNECTION_H
#define CONNECTION_H

#include <QObject>

/*
 *
 *在这个类里面获取信息
 * ("ME", "ME/Material science and engineering", "ME/Material science and engineering/Notes (Freshman&Second Semester 2019) by HuaHua.pdf", "MwCS", "MwCS/Infinitesimal Calculus", "MwCS/Infinitesimal Calculus/Stephen Abbott-Understanding Analysis.pdf.pdf", "MwCS/SetTheory", "MwCS/SetTheory/Paul R. Halmos - Naive Set Theory-Springer (1974).pdf", "CE", "CE/Analytical Chemistry", "CE/Analytical Chemistry/Notes for AC1 before exam (2019 freshman 2nd semester) by Obird.pdf", "CE/Organic Chemistry", "CE/Organic Chemistry/Machnism collection (2019 freshman 2nd semester) by OBird.pdf", "CE/Intro 2 Chemical and BIochemical Engineering", "CE/Intro 2 Chemical and BIochemical Engineering/Notes (2019 freshman 2nd semester) by OBird.pdf", "CE/Intro 2 Chemical and BIochemical Engineering/(for reference)Basic Principles and Calculations in Chemical Engineering.pdf", "BFE", "BFE/Organic Chemistry", "BFE/Organic Chemistry/Machnism collection (2019 freshman 2nd semester) by OBird.pdf", "GE(compulsory)", "GE(compulsory)/Calculus", "GE(compulsory)/Calculus/Notes for calculus2(2019 freshman 2nd semester) by OBird.pdf", "GE(compulsory)/Calculus/INTRODUCTION TO REAL ANALYSIS - Williams.pdf", "GE(compulsory)/Calculus/Calculus - Thomas.pdf", "GE(compulsory)/Chemistry", "GE(compulsory)/Linear Algebra", "GE(compulsory)/Physics", "GE(compulsory)/Physics/Fundamentals Physics.pdf")
 *  ⬆️这是初始获得的信息
 *  首先 QString中不含有 "/" 字符的为初始文件夹 以此为区分
 *
 *  第一步 先获取有多少个初始文件夹
 *  (以下算法仍有很大改进空间)
 *  第二步 创建一个QList<QStringList>作为总的List
 *  第三步 ⬆️中每个QStringList以初始文件夹名为首项，用contains方法将隶属于文件夹下的子目录放到同一个QStringList中
 *  第四部 创建接口 返回QList
 *
 *
 *
 */
#include "QSsh/sshconnection.h"
#include "QSsh/sshremoteprocessrunner.h"
#include "QSsh/sshdirecttcpiptunnel.h"
#include "QSsh/sshconnectionmanager.h"
#include <QWidget>
#include <QObject>

using namespace QSsh;

class Connection : public QObject
{
    Q_OBJECT
public:
    explicit Connection(QObject *parent = nullptr);
    ~Connection();
    QList<QStringList> getList();
    void refresh();

private:
    QList<QStringList> list;
    QStringList ll;
    SshConnection *c;
    QSharedPointer<SshRemoteProcess> s;
    void initStringList();
signals:
    void Done();
private slots:
    void afterConnection();
    void afterShellStarted();
    void afterReadOutput();

};

#endif // CONNECTION_H
