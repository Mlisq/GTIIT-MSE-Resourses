#ifndef MAINWIDGET_H
#define MAINWIDGET_H

#include <QWidget>
#include <QStandardItemModel>
#include <QStandardItem>
#include "connection.h"
QT_BEGIN_NAMESPACE
namespace Ui { class MainWidget; }
QT_END_NAMESPACE

class MainWidget : public QWidget
{
    Q_OBJECT

public:
    MainWidget(QWidget *parent = nullptr);
    ~MainWidget();
    QStandardItemModel *model;
private:
    Ui::MainWidget *ui;
    Connection c;

    void addTreeView(QStandardItem *fitem, int index,QStringList list);

private slots:

    void initTreeView();
};
#endif // MAINWIDGET_H
