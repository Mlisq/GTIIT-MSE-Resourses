#include "mainwidget.h"
#include "ui_mainwidget.h"
#include <QDebug>
#include <QString>

MainWidget::MainWidget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::MainWidget)
{
    ui->setupUi(this);
    connect(&c,&Connection::Done,this,&MainWidget::initTreeView);
}

MainWidget::~MainWidget()
{
    delete ui;
}

void MainWidget::initTreeView()
{
    QList<QStringList> l = c.getList();


    model = new QStandardItemModel(ui->treeView);
    model->setHorizontalHeaderLabels(QStringList()<<QStringLiteral("项目名"));
    for(int i = 0;i < l.size(); i ++)
    {
        if(l.at(i).endsWith(""))
            continue;
        QStringList tmp = l.at(i);
        qDebug() << tmp;
        //QStandardItem *mainI = new QStandardItem(tmp.at(0));
        //addTreeView(mainI,0,tmp);
    }
    ui->treeView->setModel(model);
}

/*
 * for (int i=0;i<l.size();i ++)
 * {
 *      QStringList tmp = l.at(i);
 *
 *
 *
 */

void MainWidget::addTreeView(QStandardItem *fitem, int index,QStringList list)
{
    QString head = fitem->text()+"/";
    for(int i = index; i < list.size(); i ++)
    {
        if(i+1 > list.size())
            break;
        QString t = list.at(i+1);
        if(t.contains(head))
        {

        }
    }
}
